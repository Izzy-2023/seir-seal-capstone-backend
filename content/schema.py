import graphene
from graphene_django.types import DjangoObjectType
from graphene_file_upload.scalars import Upload
from .models import Article

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'published_date', 'updated_date')

class Query(graphene.ObjectType):
    article = graphene.Field(ArticleType, id=graphene.Int(required=True))
    articles = graphene.List(ArticleType)

    def resolve_article(self, info, id):
        return Article.objects.get(pk=id)

    def resolve_articles(self, info):
        return Article.objects.all().order_by('-updated_date', '-published_date')

class CreateArticle(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        image = Upload()  # Add an argument for the image file

    article = graphene.Field(ArticleType)

    def mutate(self, info, title, body, image=None):
        article = Article(title=title, body=body)

        if image:
            article.image = image  # Assign the image to the article

        article.save()
        return CreateArticle(article=article)

class UpdateArticle(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        image = Upload()  # Add an argument for the image file

    article = graphene.Field(ArticleType)

    def mutate(self, info, id, title, body, image=None):
        article = Article.objects.get(pk=id)
        article.title = title
        article.body = body

        if image:
            article.image = image  # Assign the image to the article

        article.save()
        return UpdateArticle(article=article)

class DeleteArticle(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            article = Article.objects.get(pk=id)
            article.delete()
            return DeleteArticle(success=True)
        except Article.DoesNotExist:
            return DeleteArticle(success=False, error="Article not found.")
        except Exception as e:
            return DeleteArticle(success=False, error=str(e))


class Mutation(graphene.ObjectType):
    create_article = CreateArticle.Field()
    update_article = UpdateArticle.Field()
    delete_article = DeleteArticle.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

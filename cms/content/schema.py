import graphene
from graphene_django.types import DjangoObjectType
from .models import Article

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article

class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType)

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()

class CreateArticle(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)

    article = graphene.Field(ArticleType)

    def mutate(self, info, title, body):
        article = Article(title=title, body=body)
        article.save()
        return CreateArticle(article=article)

class Mutation(graphene.ObjectType):
    create_article = CreateArticle.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

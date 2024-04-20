# schema.py

import graphene
from graphene_django.types import DjangoObjectType
from .models import Article  # Ensure this import is correct

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article

class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType)
    article = graphene.Field(ArticleType, id=graphene.Int(required=True))

    def resolve_articles(self, info):
        return Article.objects.all()

    def resolve_article(self, info, id):
        return Article.objects.get(pk=id)

class CreateArticle(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)

    article = graphene.Field(ArticleType)

    def mutate(self, info, title, body):
        article = Article(title=title, body=body)
        article.save()
        return CreateArticle(article=article)

class UpdateArticle(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)
        body = graphene.String(required=True)

    article = graphene.Field(ArticleType)

    def mutate(self, info, id, title, body):
        article = Article.objects.get(pk=id)
        article.title = title
        article.body = body
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


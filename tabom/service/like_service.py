from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like | None:
    if user_id and article_id:
        Like.objects.create(user_id=user_id, article_id=article_id)
    return None


def undo_like(user_id: int, article_id: int) -> None:
    like = Like.objects.filter(user_id=user_id, article_id=article_id).get()
    like.delete()

from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like | None:
    if user_id and article_id:
        Like.objects.create(user_id=user_id, article_id=article_id)
    return None

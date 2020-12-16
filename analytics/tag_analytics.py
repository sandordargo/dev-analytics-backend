from models.tag import Tag


def get_tags_from_articles(articles):
    tags = []
    for article in articles:
        for tag_name in article.tags:
            tag_found = False
            tag_to_use = None
            for tag in tags:
                if tag.name == tag_name:
                    tag_found = True
                    tag_to_use = tag

            if not tag_found:
                new_tag = Tag(tag_name)
                tag_to_use = new_tag
                tags.append(new_tag)
            tag_to_use.register_article(article)
    return tags


def analyze(tags):
    return {
        "mostViewedTag": {
            "name": get_tag_with_most_views(tags).name,
            "count": get_tag_with_most_views(tags).views
        },
        "mostCommentedTag": {
            "name": get_tag_with_most_comments(tags).name,
            "count": get_tag_with_most_comments(tags).comments
        },
        "mostReactedTag": {
            "name": get_tag_with_most_reactions(tags).name,
            "count": get_tag_with_most_reactions(tags).reactions
        },
        "tagWithMostViewsPerArticle": {
            "name": get_most_views_per_article_tag(tags).name,
            "count": get_most_views_per_article_tag(tags).get_views_per_article()
        },
        "tagWithMostReactionsPerArticle": {
            "name": get_most_reactions_per_article_tag(tags).name,
            "count": get_most_reactions_per_article_tag(tags).get_reactions_per_article()
        },
        "tagWithMostCommentsPerArticle": {
            "name": get_most_comments_per_article_tag(tags).name,
            "count": get_most_comments_per_article_tag(tags).get_comments_per_article()
        },
    }

def get_tag_with_most_views(tags):
    return sorted(tags, reverse=True, key=lambda tag: tag.views)[0]


def get_tag_with_most_comments(tags):
    return sorted(tags, reverse=True, key=lambda tag: tag.comments)[0]


def get_tag_with_most_reactions(tags):
    return sorted(tags, reverse=True, key=lambda tag: tag.reactions)[0]


def get_views_per_article_for_each_tag(tags):
    return {tag: tag.get_views_per_article() for tag in tags}


def get_reactions_per_article_for_each_tag(tags):
    return {tag: tag.reactions / len(tag.articles) for tag in tags}


def get_comments_per_article_for_each_tag(tags):
    return {tag: tag.comments / len(tag.articles) for tag in tags}


def get_most_views_per_article_tag(tags):
    return sorted(tags, key=Tag.get_views_per_article, reverse=True)[0]


def get_most_reactions_per_article_tag(tags):
    return sorted(tags, key=Tag.get_reactions_per_article, reverse=True)[0]


def get_most_comments_per_article_tag(tags):
    return sorted(tags, key=Tag.get_comments_per_article, reverse=True)[0]

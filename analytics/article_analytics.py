def analyse(articles):
    return {
        "numberOfArticles": len(articles),
        "totalViews": get_total_views(articles),
        "totalReactions": get_total_reactions(articles),
        "totalComments": get_total_comments(articles),
        "averageViews": get_total_views(articles)/len(articles),
        "averageReactions": get_total_reactions(articles)/len(articles),
        "averageComments": get_total_comments(articles)/len(articles),
        "averageViewsForTop80Percent": get_average_views_for_top_n_percent(articles, 80),
        "averageReactionsForTop80Percent": get_average_reactions_for_top_n_percent(articles, 80),
        "averageCommentsForTop80Percent": get_average_comments_for_top_n_percent(articles, 80),
        "averageViewsForTop95Percent": get_average_views_for_top_n_percent(articles, 95),
        "averageReactionsForTop95Percent": get_average_reactions_for_top_n_percent(articles, 95),
        "averageCommentsForTop95Percent": get_average_comments_for_top_n_percent(articles, 95),
        "mostViewedArticleRatioToTotal": get_part_of_most_viewed_article_out_of_total_views(articles) * 100,
        "mostReactedArticleRatioToTotal": get_part_of_article_with_most_reactions_out_of_total_reaction(articles) * 100,
        "mostCommentedArticleRatioToTotal": get_part_of_article_with_most_comments_out_of_total_reaction(
            articles) * 100,
        "percentageOfArticlesGiving80PercentOfViews": get_ratio_of_articles_giving_top_n_percent_of_views(articles,
                                                                                                          80) * 100,
        "percentageOfArticlesGiving95PercentOfViews": get_ratio_of_articles_giving_top_n_percent_of_views(articles,
                                                                                                          95) * 100,
        "percentageOfArticlesGiving80PercentOfReactions": get_ration_of_articles_giving_top_n_percent_of_reactions(
            articles,
            80) * 100,
        "percentageOfArticlesGiving95PercentOfReactions": get_ration_of_articles_giving_top_n_percent_of_reactions(
            articles,
            95) * 100,
        "percentageOfArticlesGiving80PercentOfComments": get_ratio_of_articles_giving_top_n_percent_of_comments(
            articles,
            80) * 100,
        "percentageOfArticlesGiving95PercentOfComments": get_ratio_of_articles_giving_top_n_percent_of_comments(
            articles,
            95) * 100,
        "fiveMostViewedArticles": [article.as_json() for article in get_top_n_views(articles, 5)],
        "fiveMostReactedArticles": [article.as_json() for article in get_top_n_reactions(articles, 5)],
        "fiveMostCommentedArticles": [article.as_json() for article in get_top_n_comments(articles, 5)],
    }


def get_total_views(articles):
    return sum(article.views for article in articles)


def get_total_reactions(articles):
    return sum(article.reactions for article in articles)


def get_total_comments(articles):
    return sum(article.comments for article in articles)


def get_top_n_views(articles, top_n):
    articles.sort(key=lambda article: article.views, reverse=True)
    return articles[:top_n]


def get_top_n_comments(articles, top_n):
    articles.sort(key=lambda article: article.comments, reverse=True)
    return articles[:top_n]


def get_top_n_reactions(articles, top_n):
    articles.sort(key=lambda article: article.reactions, reverse=True)
    return articles[:top_n]


def get_average_views_for_top_n_percent(articles, top_n):
    articles.sort(key=lambda article: article.views, reverse=True)
    number_of_top_articles = get_number_of_articles_giving_top_n_percent_of(get_total_views, articles, top_n)
    return sum(article.views for article in articles[:number_of_top_articles]) / number_of_top_articles


def get_average_comments_for_top_n_percent(articles, top_n):
    articles.sort(key=lambda article: article.comments, reverse=True)
    number_of_top_articles = get_number_of_articles_giving_top_n_percent_of(get_total_views, articles, top_n)
    return sum(article.comments for article in articles[:number_of_top_articles]) / number_of_top_articles


def get_average_reactions_for_top_n_percent(articles, top_n):
    articles.sort(key=lambda article: article.reactions, reverse=True)
    number_of_top_articles = get_number_of_articles_giving_top_n_percent_of(get_total_views, articles, top_n)
    return sum(article.reactions for article in articles[:number_of_top_articles]) / number_of_top_articles


def get_ratio_of_articles_giving_top_n_percent_of_views(articles, top_n):
    articles.sort(key=lambda article: article.views, reverse=True)
    return get_ratio_of_articles_giving_top_n_percent_of(get_total_views, articles, top_n)


def get_ratio_of_articles_giving_top_n_percent_of_comments(articles, top_n):
    articles.sort(key=lambda article: article.comments, reverse=True)
    return get_ratio_of_articles_giving_top_n_percent_of(get_total_comments, articles, top_n)


def get_ration_of_articles_giving_top_n_percent_of_reactions(articles, top_n):
    articles.sort(key=lambda article: article.reactions, reverse=True)
    return get_ratio_of_articles_giving_top_n_percent_of(get_total_reactions, articles, top_n)


def get_ratio_of_articles_giving_top_n_percent_of(function, articles, top_n):
    return get_number_of_articles_giving_top_n_percent_of(function, articles, top_n) / len(articles)


def get_number_of_articles_giving_top_n_percent_of(function, articles, top_n):
    total = function(articles)
    number_of_articles = 1
    current_ratio = function(articles[:number_of_articles]) / total
    while current_ratio < top_n / 100:
        number_of_articles += 1
        current_ratio = function(articles[:number_of_articles]) / total
    return number_of_articles


def get_part_of_most_viewed_article_out_of_total_views(articles):
    articles.sort(key=lambda article: article.views, reverse=True)
    return articles[0].views / get_total_views(articles)


def get_part_of_article_with_most_reactions_out_of_total_reaction(articles):
    articles.sort(key=lambda article: article.reactions, reverse=True)
    return articles[0].reactions / get_total_reactions(articles)


def get_part_of_article_with_most_comments_out_of_total_reaction(articles):
    articles.sort(key=lambda article: article.comments, reverse=True)
    return articles[0].comments / get_total_comments(articles)

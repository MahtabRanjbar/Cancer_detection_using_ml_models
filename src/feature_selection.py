from loguru import logger
from sklearn.feature_selection import SelectKBest, f_classif


def select_features():
    # Define the feature selection method
    logger.info("Defining feature selection method")
    feature_selection = SelectKBest(f_classif)
    return feature_selection

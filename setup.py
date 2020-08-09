from setuptools import setup, find_packages

setup(
    name="twitter_bot_type_classification",
    version="0.1",
    author="infinityofspace",
    url="https://github.com/infinityofspace/twitter-bot-type-classification",
    description="Generate twitter database, calculate features and classify user",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=[
        "requests>=2.24.0",
        "numpy>=1.19.1",
        "tweepy>=3.9.0",
        "nltk>=3.5",
        "scikit-learn>=0.23.2",
        "jupyterlab>=2.2.4",
        "plotly>=4.9.0",
        "matplotlib>=3.3.0",
    ],
    entry_points={
        'console_scripts': ["twitter-bot-generate=twitter_bot_type_classification.generate_db:main",
                            "twitter-bot-features=twitter_bot_type_classification.calc_features:main"]
    }
)

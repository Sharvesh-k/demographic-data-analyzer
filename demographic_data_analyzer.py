
import pandas as pd


def calculate_demographic_data(print_data=True):
    
    df = pd.read_csv("adult.data.csv")

    
    race_count = df["race"].value_counts()

    
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )

    
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    
    advanced_education = ["Bachelors", "Masters", "Doctorate"]

    higher_education = df[
        df["education"].isin(advanced_education)
    ]

    lower_education = df[
        ~df["education"].isin(advanced_education)
    ]

    
    higher_education_rich = round(
        (higher_education["salary"] == ">50K").mean() * 100, 1
    )

    
    lower_education_rich = round(
        (lower_education["salary"] == ">50K").mean() * 100, 1
    )

    
    min_work_hours = df["hours-per-week"].min()

    
    num_min_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    
    rich_percentage = round(
        (num_min_workers["salary"] == ">50K").mean() * 100, 1
    )

    
    country_count = df["native-country"].value_counts()

    country_rich = df[
        df["salary"] == ">50K"
    ]["native-country"].value_counts()

    country_percentage = (
        country_rich / country_count * 100
    )

    highest_earning_country = country_percentage.idxmax()

    highest_earning_country_percentage = round(
        country_percentage.max(), 1
    )

    
    top_IN_occupation = df[
        (df["native-country"] == "India")
        & (df["salary"] == ">50K")
    ]["occupation"].value_counts().idxmax()

    
    result = {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education": higher_education,
        "lower_education": lower_education,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }

    if print_data:
        for key, value in result.items():
            print(f"{key}: {value}")

    return result

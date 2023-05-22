import csv
import sys
from os.path import abspath, dirname

from sqlalchemy.orm import Session

sys.path.append(dirname(dirname(abspath(__file__))))
from app.db import engine  # noqa
from app.models import Base, Compensation  # noqa


def migrate_from_csv(path: str) -> None:
    session = Session(engine)

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            compensation = Compensation(
                timestamp=row["Timestamp"],
                employment_type=row["Employment Type"],
                company_name=row["Company Name"],
                company_size=row["Company Size - # Employees"],
                primary_location_country=row["Primary Location (Country)"],
                primary_location_city=row["Primary Location (City)"],
                industry_in_company=row["Industry in Company"],
                public_or_private_company=row["Public or Private Company"],
                years_experience_in_industry=row["Years Experience in Industry"],
                years_of_experience_in_current_company=row[
                    "Years of Experience in Current Company  "
                ],
                job_title_in_company=row["Job Title In Company"],
                job_ladder=row["Job Ladder"],
                job_level=row["Job Level"],
                required_hours_per_week=row["Required Hours Per Week"],
                actual_hours_per_week=row["Actual Hours Per Week"],
                highest_level_of_formal_education_completed=row[
                    "Highest Level of Formal Education Completed"
                ],
                total_base_salary_in_2018=row["Total Base Salary in 2018 (in USD)"],
                total_bonus_in_2018=row[
                    "Total Bonus in 2018 (cumulative annual value in USD)"
                ],
                total_stock_options_equity_in_2018=row[
                    "Total Stock Options/Equity in 2018 (cumulative annual value in USD)"
                ],
                health_insurance_offered=row["Health Insurance Offered"],
                annual_vacation_in_weeks=row["Annual Vacation (in Weeks)"],
                happiness_at_current_position=row[
                    "Are you happy at your current position?"
                ],
                plan_to_resign_in_next_12_months=row[
                    "Do you plan to resign in the next 12 months?"
                ],
                thoughts_about_direction_of_your_industry=row[
                    "What are your thoughts about the direction of your industry?"
                ],
            )
            session.add(compensation)

    session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    migrate_from_csv("datasets/salary_survey.csv")

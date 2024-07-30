from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def generate_cars_name(file_path):
    # Read company names from the file
    with open(file_path, 'r') as file:
        company_names = file.readlines()

    # Strip newline characters from each company name
    company_names = [name.strip() for name in company_names]

    return company_names

def generate_prompt(car_name):
    return f"""You are an AI assistant. I need detailed information on {car_name} car in Canada. Please provide the following details for each model:
        1. Model Name
        2. Year
        3. Starting Price
        4. Engine Options
        5. Key Features
        6. Available Trims
        7. Fuel Economy (City/Highway)
        8. Safety Ratings
        9. Warranty Information
        10. Financial Rate
        11. Lease Rate
        12. Type (e.g., SUV, Sedan, Hybrid/Electric)
        13. Link to Official Webpage for Each Model

        Please format the information in a clear and organized manner."""

# Function to send a prompt to GPT and get the response
def get_gpt_response(prompt):
    client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


def generate_car_information(car_name, output_file):

    prompt = generate_prompt(car_name)
    gpt_response = get_gpt_response(prompt)

    with open(output_file, 'a') as file:
        file.write(f"\n{gpt_response}\n")
        file.write("="*80 + "\n")



if __name__ == "__main__":
    carNames_file_path = 'src\materials\CarNames.txt'
    carsInformation_file_path = 'src\materials\CarsInformation.txt'

    cars_name = generate_cars_name(carNames_file_path)
    
    for car in cars_name:
        generate_car_information(car, carsInformation_file_path)

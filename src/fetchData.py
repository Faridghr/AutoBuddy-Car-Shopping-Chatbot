from openai import OpenAI
from dotenv import load_dotenv
import os



class FetchData():
    load_dotenv()

    def __init__(self):
        pass

    def generate_cars_group(self, file_path):
        # Read company names from the file
        with open(file_path, 'r') as file:
            company_names = file.read().strip()

        # Strip newline characters from each company name
        groups_car = company_names.split('\n\n')
        return groups_car
    
    def generate_cars_name(self, group):
        result = ''
        group_list = group.split('\n')
        for i in group_list:
            result = result + i + ', '
        result = result[:-2]
        return result

    def generate_prompt(self, car_name):
        return f"""You are an AI assistant. I need detailed information on {car_name} cars in Canada 2024. Please provide the following details for each model:
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
    def get_gpt_response(self, prompt):
        client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content


    def generate_car_information(self, car_name, output_file):

        prompt = self.generate_prompt(car_name)
        gpt_response = self.get_gpt_response(prompt)

        with open(output_file, 'a') as file:
            file.write(f"\n{gpt_response}\n")
            file.write("="*80 + "\n")



if __name__ == "__main__":

    fetchData = FetchData()

    carNames_file_path = 'src\materials\Car_models_available_in_Canada_for_2024.txt'
    carsInformation_file_path = 'src\materials\CarsInformation.txt'

    cars_name_groups = fetchData.generate_cars_group(carNames_file_path)

    #print(len(cars_name_groups))

    for group in cars_name_groups:
        cars_name = fetchData.generate_cars_name(group)
        fetchData.generate_car_information(cars_name, carsInformation_file_path)


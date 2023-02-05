from recipe_scrapers import scrape_me
import openai
import json

#Open AI Key
openai.api_key = ""

def parse_menu(url):
    #Grabbing link for recipe
    scraper = scrape_me(url)

    #First part of prompt
    pre_question = "\n\nI am a recipe ingredient scraping bot. My purpose is to convert natural-language ingredients list into formatted JSON output. Given the following input: \n"

    #List refernce
    reference = ['2 large eggs', 'Pinch fine sea salt', '1/2 Tbsp unsalted butter', '1/4 cup shredded mozzarella (low moisture, part-skim)']
    ref_formatted = "\n".join([f'\'{thing}\',' for thing in reference])
    print("FORMATTED JSON --> \n" + ref_formatted)
    scraper_formatted = "\n".join([f'\'{thing}\',' for thing in scraper.ingredients()])

    #Opening json reference
    with open("./extract_correct.json") as file:
        extract_correct = json.load(file)
        print("CORRECT JSON --> \n" + json.dumps(extract_correct))

    #Forming question
    question = pre_question + ref_formatted + "\n and I will produce the following JSON output: \n" + json.dumps(extract_correct) + "\n and my new input is: \n" + scraper_formatted
    print(question)

    #Asking question
    response = openai.Completion.create(model="text-davinci-003", prompt=question, temperature=0, max_tokens=100)

    #Printing question
    print(response)
    return(response)

parse_menu('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
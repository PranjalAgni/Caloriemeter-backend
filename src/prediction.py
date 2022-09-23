from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import os


def generate_foodlist():
    food_list = [
        "apple_pie",
        "baby_back_ribs",
        "baklava",
        "beef_carpaccio",
        "beef_tartare",
        "beet_salad",
        "beignets",
        "bibimbap",
        "bread_pudding",
        "breakfast_burrito",
        "bruschetta",
        "caesar_salad",
        "cannoli",
        "caprese_salad",
        "carrot_cake",
        "ceviche",
        "cheese_plate",
        "cheesecake",
        "chicken_curry",
        "chicken_quesadilla",
        "chicken_wings",
        "chocolate_cake",
        "chocolate_mousse",
        "churros",
        "clam_chowder",
        "club_sandwich",
        "crab_cakes",
        "creme_brulee",
        "croque_madame",
        "cup_cakes",
        "deviled_eggs",
        "donuts",
        "dumplings",
        "edamame",
        "eggs_benedict",
        "escargots",
        "falafel",
        "filet_mignon",
        "fish_and_chips",
        "foie_gras",
        "french_fries",
        "french_onion_soup",
        "french_toast",
        "fried_calamari",
        "fried_rice",
        "frozen_yogurt",
        "garlic_bread",
        "gnocchi",
        "greek_salad",
        "grilled_cheese_sandwich",
        "grilled_salmon",
        "guacamole",
        "gyoza",
        "hamburger",
        "hot_and_sour_soup",
        "hot_dog",
        "huevos_rancheros",
        "hummus",
        "ice_cream",
        "lasagna",
        "lobster_bisque",
        "lobster_roll_sandwich",
        "macaroni_and_cheese",
        "macarons",
        "miso_soup",
        "mussels",
        "nachos",
        "omelette",
        "onion_rings",
        "oysters",
        "pad_thai",
        "paella",
        "pancakes",
        "panna_cotta",
        "peking_duck",
        "pho",
        "pizza",
        "pork_chop",
        "poutine",
        "prime_rib",
        "pulled_pork_sandwich",
        "ramen",
        "ravioli",
        "red_velvet_cake",
        "risotto",
        "samosa",
        "sashimi",
        "scallops",
        "seaweed_salad",
        "shrimp_and_grits",
        "spaghetti_bolognese",
        "spaghetti_carbonara",
        "spring_rolls",
        "steak",
        "strawberry_shortcake",
        "sushi",
        "tacos",
        "takoyaki",
        "tiramisu",
        "tuna_tartare",
        "waffles",
    ]

    return food_list


# model location
model_location = os.path.abspath(os.path.join("src", "models", "model_epoch_8.hdf5"))
print(f"\n\n\n Model location {model_location}\n\n\n")
# loading the model
model = load_model(model_location, compile=False)
# generating the foodlist from the directory
food_list = generate_foodlist()
food_list.sort()


def get_top_k_predictions(num_predictions: int, predictions):
    top_k_values, top_k_indices = tf.nn.top_k(predictions, k=num_predictions)
    top_k_food_items = [food_list[index] for index in top_k_indices[0]]
    return top_k_food_items


def preprocess_image(input_image: str):
    input_image = image.load_img(input_image, target_size=(299, 299))
    input_image = image.img_to_array(input_image)
    input_image = np.expand_dims(input_image, axis=0)
    input_image /= 255
    return input_image


def predict_food_item(input_image_location: str):
    preprocessed_image = preprocess_image(input_image_location)
    prediction = model.predict(preprocessed_image)
    k_food_predictions = get_top_k_predictions(5, prediction)
    print(f"This is the prediction {get_top_k_predictions(5, prediction)}")
    # index = np.argmax(prediction)
    return k_food_predictions


def remove_file(input_image_location: str):
    os.unlink(input_image_location)

import json

data = {
    "questions": [{
        "type": "mcq",
        "question": "Which of the following microorganisms causes malaria?",
        "options": ["Virus", "Bacteria", "Protozoa", "Fungi"],
        "answer": "Protozoa"
    }, {
        "type": "mcq",
        "question": "Yeast is used in the production of:",
        "options": ["Vinegar", "Antibiotics", "Cheese", "Bread"],
        "answer": "Bread"
    }, {
        "type": "mcq",
        "question": "Antibiotics are effective against:",
        "options": ["Viruses", "Fungi", "Bacteria", "Protozoa"],
        "answer": "Bacteria"
    }, {
        "type":
        "mcq",
        "question":
        "The process of conversion of sugar into alcohol is called:",
        "options":
        ["Fermentation", "Decomposition", "Photosynthesis", "Respiration"],
        "answer":
        "Fermentation"
    }, {
        "type":
        "mcq",
        "question":
        "Which of the following microorganisms is used in the production of antibiotics?",
        "options":
        ["Penicillium", "Saccharomyces", "Lactobacillus", "Rhizobium"],
        "answer":
        "Penicillium"
    }, {
        "type": "mcq",
        "question":
        "Which microorganism is responsible for fixing nitrogen in the soil?",
        "options": ["Rhizobium", "Penicillium", "Yeast", "Amoeba"],
        "answer": "Rhizobium"
    }, {
        "type": "mcq",
        "question": "Anthrax is caused by:",
        "options": ["Virus", "Bacteria", "Protozoa", "Fungi"],
        "answer": "Bacteria"
    }, {
        "type": "mcq",
        "question": "Which microorganism causes the disease cholera?",
        "options": ["Virus", "Bacteria", "Protozoa", "Fungi"],
        "answer": "Bacteria"
    }, {
        "type":
        "mcq",
        "question":
        "The process of conversion of milk into curd is due to the action of:",
        "options":
        ["Rhizobium", "Lactobacillus", "Penicillium", "Saccharomyces"],
        "answer":
        "Lactobacillus"
    }, {
        "type": "mcq",
        "question":
        "Which microorganism is used in the biological treatment of sewage?",
        "options": ["Algae", "Virus", "Bacteria", "Fungi"],
        "answer": "Bacteria"
    }, {
        "type": "mcq",
        "question": "Ringworm is caused by:",
        "options": ["Virus", "Bacteria", "Fungi", "Protozoa"],
        "answer": "Fungi"
    }, {
        "type": "mcq",
        "question": "HIV (Human Immunodeficiency Virus) causes:",
        "options": ["Common cold", "Tuberculosis", "AIDS", "Cholera"],
        "answer": "AIDS"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the preparation of idli and dosa batter?",
        "options":
        ["Rhizobium", "Saccharomyces", "Lactobacillus", "Aspergillus"],
        "answer":
        "Lactobacillus"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the production of biogas?",
        "options": ["Methanogens", "Rhizobium", "Penicillium", "Algae"],
        "answer":
        "Methanogens"
    }, {
        "type": "mcq",
        "question": "Tetanus is caused by:",
        "options": ["Bacteria", "Virus", "Protozoa", "Fungi"],
        "answer": "Bacteria"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the production of antibiotics such as streptomycin?",
        "options":
        ["Rhizobium", "Penicillium", "Saccharomyces", "Lactobacillus"],
        "answer":
        "Streptomyces"
    }, {
        "type":
        "mcq",
        "question":
        "Which of the following microorganisms helps in nitrogen fixation in leguminous plants?",
        "options":
        ["Rhizobium", "Penicillium", "Saccharomyces", "Aspergillus"],
        "answer":
        "Rhizobium"
    }, {
        "type": "mcq",
        "question": "Which microorganism causes athlete's foot?",
        "options": ["Virus", "Bacteria", "Fungi", "Protozoa"],
        "answer": "Fungi"
    }, {
        "type": "mcq",
        "question": "The disease 'dengue' is caused by:",
        "options": ["Virus", "Bacteria", "Protozoa", "Fungi"],
        "answer": "Virus"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the preparation of antibiotics like penicillin?",
        "options":
        ["Rhizobium", "Penicillium", "Saccharomyces", "Lactobacillus"],
        "answer":
        "Penicillium"
    }, {
        "type": "mcq",
        "question": "Which microorganism causes food poisoning?",
        "options": ["Virus", "Bacteria", "Protozoa", "Fungi"],
        "answer": "Bacteria"
    }, {
        "type":
        "mcq",
        "question":
        "Which of the following is a beneficial role of microorganisms in agriculture?",
        "options": [
            "Causing diseases in crops", "Reducing soil fertility",
            "Fixing nitrogen in the soil", "Increasing soil erosion"
        ],
        "answer":
        "Fixing nitrogen in the soil"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the production of antibiotics such as tetracycline?",
        "options":
        ["Rhizobium", "Penicillium", "Saccharomyces", "Streptomyces"],
        "answer":
        "Streptomyces"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the production of alcohol?",
        "options":
        ["Rhizobium", "Penicillium", "Saccharomyces", "Lactobacillus"],
        "answer":
        "Saccharomyces"
    }, {
        "type": "mcq",
        "question": "Which of the following diseases is caused by a virus?",
        "options": ["Tuberculosis", "Cholera", "AIDS", "Typhoid"],
        "answer": "AIDS"
    }, {
        "type": "mcq",
        "question": "Which microorganism causes dental caries?",
        "options": ["Virus", "Bacteria", "Protozoa", "Fungi"],
        "answer": "Bacteria"
    }, {
        "type":
        "mcq",
        "question":
        "The process of conversion of nitrogen gas into nitrates is called:",
        "options":
        ["Nitrogen fixation", "Fermentation", "Photosynthesis", "Respiration"],
        "answer":
        "Nitrogen fixation"
    }, {
        "type": "mcq",
        "question":
        "Which microorganism is used in the treatment of industrial effluents?",
        "options": ["Algae", "Virus", "Bacteria", "Fungi"],
        "answer": "Bacteria"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the baking industry?",
        "options":
        ["Rhizobium", "Penicillium", "Saccharomyces", "Lactobacillus"],
        "answer":
        "Saccharomyces"
    }, {
        "type": "mcq",
        "question": "Which of the following is a disease caused by bacteria?",
        "options": ["Measles", "Typhoid", "AIDS", "Influenza"],
        "answer": "Typhoid"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the production of vinegar?",
        "options":
        ["Rhizobium", "Penicillium", "Saccharomyces", "Acetobacter"],
        "answer":
        "Acetobacter"
    }, {
        "type": "mcq",
        "question": "Which of the following diseases is caused by protozoa?",
        "options": ["Malaria", "Tuberculosis", "Cholera", "AIDS"],
        "answer": "Malaria"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the preparation of antibiotics like erythromycin?",
        "options":
        ["Rhizobium", "Penicillium", "Saccharomyces", "Streptomyces"],
        "answer":
        "Streptomyces"
    }, {
        "type": "mcq",
        "question": "Which microorganism causes the disease tuberculosis?",
        "options": ["Virus", "Bacteria", "Protozoa", "Fungi"],
        "answer": "Bacteria"
    }, {
        "type":
        "mcq",
        "question":
        "The process of decomposition of complex organic substances into simpler ones is known as:",
        "options":
        ["Fermentation", "Respiration", "Decomposition", "Photosynthesis"],
        "answer":
        "Decomposition"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is responsible for the formation of curd from milk?",
        "options":
        ["Rhizobium", "Lactobacillus", "Penicillium", "Saccharomyces"],
        "answer":
        "Lactobacillus"
    }, {
        "type":
        "mcq",
        "question":
        "Which of the following is a role of microorganisms in maintaining soil fertility?",
        "options": [
            "Causing plant diseases", "Fixing nitrogen in soil",
            "Preventing erosion", "Reducing soil pH"
        ],
        "answer":
        "Fixing nitrogen in soil"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the production of antibiotics such as neomycin?",
        "options":
        ["Rhizobium", "Penicillium", "Streptomyces", "Lactobacillus"],
        "answer":
        "Streptomyces"
    }, {
        "type": "mcq",
        "question":
        "Which microorganism is responsible for causing diseases like ringworm?",
        "options": ["Virus", "Bacteria", "Protozoa", "Fungi"],
        "answer": "Fungi"
    }, {
        "type": "mcq",
        "question": "Which of the following diseases is caused by a virus?",
        "options": ["Typhoid", "Tuberculosis", "AIDS", "Cholera"],
        "answer": "AIDS"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the production of enzymes for commercial purposes?",
        "options":
        ["Rhizobium", "Penicillium", "Aspergillus", "Saccharomyces"],
        "answer":
        "Aspergillus"
    }, {
        "type": "mcq",
        "question":
        "Which microorganism is used in the bioremediation of oil spills?",
        "options": ["Algae", "Virus", "Bacteria", "Fungi"],
        "answer": "Algae"
    }, {
        "type":
        "mcq",
        "question":
        "Which of the following is a beneficial role of microorganisms in the nitrogen cycle?",
        "options": [
            "Reducing soil fertility", "Fixing nitrogen in the soil",
            "Causing soil erosion", "Preventing nutrient cycling"
        ],
        "answer":
        "Fixing nitrogen in the soil"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the production of antibiotics such as cephalosporin?",
        "options":
        ["Rhizobium", "Penicillium", "Saccharomyces", "Streptomyces"],
        "answer":
        "Streptomyces"
    }, {
        "type": "mcq",
        "question":
        "Which microorganism is used in the treatment of sewage water?",
        "options": ["Algae", "Virus", "Bacteria", "Fungi"],
        "answer": "Bacteria"
    }, {
        "type": "mcq",
        "question": "Which of the following is a disease caused by protozoa?",
        "options": ["Cholera", "Tuberculosis", "Malaria", "AIDS"],
        "answer": "Malaria"
    }, {
        "type":
        "mcq",
        "question":
        "Which microorganism is used in the production of antibiotics such as vancomycin?",
        "options":
        ["Rhizobium", "Penicillium", "Saccharomyces", "Streptomyces"],
        "answer":
        "Streptomyces"
    }, {
        "type": "mcq",
        "question": "Which microorganism causes the disease tetanus?",
        "options": ["Virus", "Bacteria", "Protozoa", "Fungi"],
        "answer": "Bacteria"
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Microorganisms are too small to be seen with the naked eye.",
        "reason":
        "Reason: They are typically measured in micrometers (\u00b5m), which are millionths of a meter.",
        "answer":
        "Assertion is correct, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: All microorganisms are harmful to humans.",
        "reason":
        "Reason: Some microorganisms cause diseases like the common cold.",
        "answer":
        "Assertion is wrong, reason is correct (but not all microorganisms cause disease)."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Bacteria can be single-celled or multicellular.",
        "reason":
        "Reason: All living things are either single-celled or multicellular.",
        "answer":
        "Assertion is wrong, reason is not generally true (bacteria are always single-celled)."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Antibiotics treat diseases caused by viruses.",
        "reason":
        "Reason: Antibiotics kill bacteria, not viruses.",
        "answer":
        "Assertion is wrong, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Bacteria are essential for yogurt production.",
        "reason":
        "Reason: Bacteria ferment lactose sugar in milk, producing lactic acid that gives yogurt its tangy taste and thick texture.",
        "answer":
        "Assertion and reason both are correct, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Molds are a type of fungus that can cause food spoilage.",
        "reason":
        "Reason: Molds grow thread-like structures called hyphae that penetrate and decompose food.",
        "answer":
        "Assertion and reason both are correct, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Yeast is a microorganism used in bread production.",
        "reason":
        "Reason: Yeast releases carbon dioxide gas during fermentation, causing the dough to rise.",
        "answer":
        "Assertion and reason both are correct, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Vaccines can prevent diseases caused by microorganisms.",
        "reason":
        "Reason: Vaccines expose the body to weakened or inactive forms of a microorganism, helping it develop immunity.",
        "answer":
        "Assertion and reason both are correct, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Microorganisms cannot be used to clean up environmental issues.",
        "reason":
        "Reason: Some bacteria can break down oil into harmless substances, aiding in oil spill cleanup.",
        "answer":
        "Assertion is wrong, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: All microorganisms reproduce asexually.",
        "reason":
        "Reason: Some microorganisms, like bacteria, can reproduce by binary fission, where one cell divides into two.",
        "answer":
        "Assertion is wrong, reason is correct (but not all microorganisms reproduce asexually)."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Microorganisms are not found in extreme environments.",
        "reason":
        "Reason: Some bacteria can survive in hot springs, while others thrive in the freezing Antarctic conditions.",
        "answer":
        "Assertion is wrong, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Disinfection kills most microorganisms, but not spores.",
        "reason":
        "Reason: Sterilization is the process of killing all microorganisms, including spores, and is necessary for surgical equipment to prevent infections.",
        "answer":
        "Assertion is wrong, reason clarifies the difference between disinfection and sterilization."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Food preservation methods like pickling and drying do not prevent microbial growth.",
        "reason":
        "Reason: These methods remove moisture or create acidic conditions that inhibit microbial activity.",
        "answer":
        "Assertion is wrong, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Decomposers are not microorganisms.",
        "reason":
        "Reason: Decomposers, like some bacteria and fungi, break down dead organisms and return nutrients to the soil, maintaining soil fertility and supporting plant growth.",
        "answer":
        "Assertion is wrong, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Antibiotics are a good first line of defense for any illness.",
        "reason":
        "Reason: Overuse of antibiotics can lead to antibiotic resistance in bacteria, making them less effective in the future.",
        "answer":
        "Assertion is wrong, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Microorganisms do not play a role in the nitrogen cycle.",
        "reason":
        "Reason: Nitrogen-fixing bacteria in the soil convert nitrogen gas (N\u2082) into ammonia (NH\u2083), making it usable for plants.",
        "answer":
        "Assertion is wrong, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Probiotics are not live microorganisms.",
        "reason":
        "Reason: They are live microorganisms that offer health benefits when consumed, such as improving gut health and digestion.",
        "answer":
        "Assertion is wrong, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: All fungi are harmful to plants.",
        "reason":
        "Reason: Some fungi can cause plant diseases like mildew.",
        "answer":
        "Assertion is wrong, reason is partially correct (some fungi are harmful, but others are beneficial)."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Parasites are microorganisms that live on or in another organism and obtain nutrients from it.",
        "reason":
        "Reason: Tapeworms are an example of a parasite that lives in the human intestines and absorbs nutrients from food we eat.",
        "answer":
        "Assertion and reason both are correct, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Viruses are smaller than bacteria and cannot reproduce on their own.",
        "reason":
        "Reason: Viruses invade host cells and use the host's machinery to replicate.",
        "answer":
        "Assertion and reason both are correct, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Vaccines can only prevent viral diseases.",
        "reason":
        "Reason: Vaccines work by exposing the body to weakened or inactive forms of a pathogen, training the immune system to recognize and fight it. This can apply to viruses and some bacteria.",
        "answer":
        "Assertion is wrong, reason is partially correct (vaccines can target various pathogens)."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Microorganisms are responsible for the process of photosynthesis.",
        "reason":
        "Reason: Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to produce food (glucose) and oxygen. This process is carried out by plant cells, not microorganisms.",
        "answer":
        "Assertion is wrong, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Microbes in the human gut play a crucial role in digestion and immune function.",
        "reason":
        "Reason: The gut microbiome, a complex community of bacteria and other microbes, aids in breaking down food, absorbing nutrients, and protecting against harmful pathogens.",
        "answer":
        "Assertion and reason both are correct, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Bioplastics are a type of plastic made from non-renewable resources.",
        "reason":
        "Reason: Some bioplastics are produced from microorganisms using renewable resources like plant starches or sugars.",
        "answer":
        "Assertion is wrong, reason is correct explanation."
    }, {
        "type":
        "assertion",
        "question":
        "Assertion: Studying microorganisms can lead to advancements in medicine and biotechnology.",
        "reason":
        "Reason: Microorganisms are used in the development of new antibiotics, vaccines, and other biotechnologies with potential applications in healthcare and environmental remediation.",
        "answer":
        "Assertion and reason both are correct, reason is correct explanation."
    }]
}

for thing in data["questions"]:
    if thing["type"] == "mcq":
        continue
    thing["options"] = [
        "Assertion and reason both are correct statement and reason is correct explanation for assertion.",
        "Assertion and reason both are correct statement and reason is not correct explanation for assertion.",
        "Assertion is correct statement but reason is wrong statement.",
        "Assertion is wrong statement but reason is correct statement."
    ]
    if "reason" in thing:
        print("OK")
        del thing["reason"]
with open("question.json", "w") as f:
    json.dump(data, f, indent=4)

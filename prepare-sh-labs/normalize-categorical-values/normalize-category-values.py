'''https://prepare.sh/interview/devops/674eb80f473242bc582e99d6'''

def normalize_categorical_values(category:str) -> int:
    # normalized category
    normalized_category = category.lower()
    
    # mapping of normalized category with numberical values
    category_mapping = {
        'low': 1,
        'medium': 2,
        'high': 3
    }
    
    if normalized_category in category_mapping:
        return category_mapping[normalized_category]
    else:
        # Raise exception if the category is not recognized
        raise ValueError(f"Invalid category: '{category}'. It should be one of the following: [low, medium, high]")

def main():
    print(normalize_categorical_values(input()))
    
if __name__ == '__main__':
    main()
## Overview

Welcome to the English Dictionary repository! This project provides a simple and effective English dictionary that you can use to look up word definitions quickly. The dictionary is designed to be user-friendly and accessible for anyone who wants to enhance their vocabulary or find meanings of words. This dictionary is powered by a api created on the local machine using a json file for the data.

## Features

- **User-Friendly Interface:** The dictionary provides a clean and intuitive interface for users to easily search for word definitions. The interface is created using CustomTkinter.

- **Fast and Efficient:** The dictionary is built to deliver quick and accurate results, making it a reliable tool for users looking for instant information. To generate result at a faster rate Api is used.

- **Comprehensive Definitions:** Get detailed definitions, part-of-speech information, and example sentences for a better understanding of each word. The json file contains all the data.

## Getting Started

To use the English Dictionary, follow these steps:

1. **Clone the Repository:**
   ```
   git clone https://github.com/kumawatvaibhav/English-Dictionary.git
   ```

2. **Navigate to the Project Directory:**
   ```
   cd English-Dictionary
   ```

3. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```
   python Eng_Dic.py
   ```

5. **Enter a Word:**
   - Once the application is running, enter the word you want to look up and press Enter.

6. **View Results:**
   - The dictionary will display the definition, part of speech, and example sentences for the entered word.

## MyApi File

The `MyApi` file contains the code of the API which is the backend for fetching word and their definitions. The API is fetching data from the file `dictionary_compact.json` and making it available to the local host. This api file will automatically run as you start the Main file[`Eng_Dic.py`] and fetch you the required data from the json file.



## Contributing

If you would like to contribute to the development of this project, please do.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to explore, use, and enhance the English Dictionary 📚✨.

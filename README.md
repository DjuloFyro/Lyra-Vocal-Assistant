<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!--<a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>-->

  <h1 align="center">Lyra-Vocal-Assistant</h1>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


The goal of this project is to create a voice assistant with the power of LLMs provided by OpenAI, without the constraint of being limited to information only up to 2021. This means that the voice assistant will have agents capable of searching for complex answers on the internet to help respond to user queries.




### Built With

* ![Python][Python.js]
* ![LangChain][LangChain.js]





<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
```sh
git clone https://github.com/DjuloFyro/Lyra-Vocal-Assistant.git
```
2. Get a API Key at [https://openai.com/](https://openai.com/)
3. Export the Key as an environment variable
```sh
export OPENAI_API_KEY='yourkey'
```
4. Export also Google keys
  ```sh
export GOOGLE_CSE_ID="yourkey"
export GOOGLE_API_KEY="yourkey"
```
5. Install all packages
```sh
pip install -r requirements.txt
```


<!-- USAGE EXAMPLES -->
## Usage

```sh
python src/main.py
```
Then you can talk with the vocal assistant


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact

Julian Gil - juliangil2424@gmail.com




<!-- MARKDOWN LINKS & IMAGES -->
[Python.js]: https://img.shields.io/badge/Python-20232A?style=for-the-badge&logo=python&logoColor=61DAFB
[LangChain.js]: https://img.shields.io/badge/LangChain-35495E?style=for-the-badge&logo=langchain&logoColor=4FC08D

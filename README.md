# CryptoPortfolioManager
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) </br>
A CLI Tool to manage and track your crypto portfolio

## Requirements
Pycoingecko </br>
termcolor </br>

## Installation and Setup

Clone the repository.
```
git clone https://github.com/srivathsanvenkateswaran/CryptoPortfolioManager
```
Then navigate into the directory
```
cd CryptoPortfolioManager
```
Install the requirements with the help of requirements.txt
```
pip install -r requirements.txt
```
Now run the cryptoPortfolioManager.py file
```
python3 cryptoPortfolioManager.py
```
## Usage

```
python3 cryptoPortfolioManager.py [OPTIONS]..
```
List of available options: </br>
|```No options specified``` | Displays portfolio data alone.|
|```-h or --help```         | Displays list of available options.|
|```-w or --weightage```    | Shows the Portfolio along with the coin weightage in portfolio.|
## Tip
You can create a file and place it in ```/usr/bin``` directory and execute it as a terminal command. </br>
Here's how you can do so. </br>
```
cp cryptoPortfolioManager.py crypto
```
Open the file in nano editor
```
nano crypto
```
Now add the following line on top of the crypto file
```
#!/usr/bin/python3
```
Then move the cryto file to ```/usr/bin```.
```
sudo cp crypto /usr/bin
```
Now you can use it as a terminal command. </br></br>

Feel free to ping me in case of any doubts!!

## Sample Screenshots

Sample of a csv file containing details of a sample portfolio. </br>

![Porfolio CSV File](https://user-images.githubusercontent.com/74530357/152295450-bd6c333f-bf08-44ef-8bc6-a9b5120c3149.png)

Sample portfolio

![Sample Porftolio](https://user-images.githubusercontent.com/74530357/152295457-ee7559b4-7969-4cf6-bd2e-4c3b5c95e343.png)

Portfolio Coin Weightage

![Porfolio Coin Weightage](https://user-images.githubusercontent.com/74530357/155284845-1eb3d9b5-d3f5-446f-a484-8d3d7752487a.png)

## Sample GIF

![CryptoPortfolioManager](https://user-images.githubusercontent.com/74530357/152296017-ad21c6c3-2d43-4e5a-ae90-d9d076e5518c.gif)

## Full video

https://user-images.githubusercontent.com/74530357/152295608-c76812a0-9130-446d-958b-301b86f9150e.mp4

# Star Wars Characters

This project is a Node.js script that prints all characters of a specified Star Wars movie using the Star Wars API (SWAPI).

## Getting Started

### Prerequisites

Make sure you have Node.js and npm installed. You can check if they are installed by running the following commands:

```sh
node -v
npm -v

If you don't have Node.js and npm installed, you can download and install them from Node.js official website.

### Installation

1. Clone the repository or download the script.

2. Navigate to the project directory:

```sh
cd starwars_characters

3. Install the required npm package:
```sh
npm install request

### Usage
To run the script, use the following command:

```sh
./0-starwars_characters.js <Movie ID>

For example, to get the characters from "Return of the Jedi" (Movie ID 3), run:
```sh
./0-starwars_characters.js 3


### Example Output
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna


### Script Explanation
The script fetches the details of a specified Star Wars movie from the SWAPI, extracts the list of character URLs, fetches each character's details, and prints their names.

### Author
This project is created by Dr. Appiagyei.
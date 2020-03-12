window.addEventListener('load', init);



//Globals
let time = 5;
let score = 0;
let isPlaying;

//DOM Elements
const wordInput = document.querySelector('#word-input');
const currentWord = document.querySelector('#current-word');
const scoreDisplay = document.querySelector('#score');
const timeDisplay = document.querySelector('#time');
const message = document.querySelector('#message');
const seconds = document.querySelector('#seconds');

const words = ['tomorrow', 'rio', 'phone', 'pelican', 'orange', 'summer', 'may', 'mango', 'sweaty', 'clean', 'habit', 'bathing', 'morning'];

//Initalize game
function init(){
	//Load word from array
	showWord(words);
	// Start matching on word input
	wordInput.addEventListener('input', startMatch);
	// call countdown every second
	setInterval(countdown, 1000);
	//Check game status
	setInterval(checkStatus, 50);

}

//Start Match
function startMatch(){
	if(matchWords())
	{
		isPlaying = true;
		time = 6;
		showWord(words);
		wordInput.value = '';
		score++;

	}
	//If score is -1, display 0
	if(score == -1)
	{
		scoreDisplay.innerHTML = 0;
	}
	else
	{
		scoreDisplay.innerHTML = score;
	}	

}

//match currentWord to wordInput
function matchWords(){

	if(wordInput.value == currentWord.innerHTML)
	{
		message.innerHTML = "Correct";
		return true;
	}
	else{
		message.innerHTML = "Wrong";
		return false;
	}	
	
}


//Pick and show random word
function showWord(words) {
	//Generate random array index
	const randIndex = Math.floor(Math.random() * words.length);
	//Output random word
	currentWord.innerHTML = words[randIndex];
}

//Countdown Timer
function countdown(){
	//make sure time is run out
	if(time>0)
	{
		//decrement the time
		time--;
	}
	else if(time==0)
	{
		//Game is over
		isPlaying = false;
	}
	//Show time
	timeDisplay.innerHTML = time;

}

//Check game status
function checkStatus(){
	if(!isPlaying && time == 0)
	{
		message.innerHTML = "Game Over"
		score = -1
	}
}





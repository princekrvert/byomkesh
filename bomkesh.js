#!/usr/bin/node
//Author prince kumar
//Date 16 nov 2021
//this tool is made only for educational purpuses , i ma not responsible for any illegal activity...
//Import all the requirements...
const axios = require("axios");
const os = require("os");
const process = require("process");
const regx = require("regx");
//Make a functuon to hamdle the user requests.

function osType(){
	if ( os.type() == "Linux"){
		if ( os.platform() == "android" ){
			return "android";

		}
		else{
			return "kali";
		}
	
	}
	else{
		return "win";
	}

}
// Make a help function.. 
function help(){
	console.log("\033[0;1m This is help fun");


}
// Make a function to request the urls
function isOk(surl){
	axios.get(surl)
	.then((res)=>{
		console.log(`${res.status}`);
	//	if(res.status === 200){
		//	console.log("\033[36;1m [200 ok] \033[0;1m \t %s ", surl);}
	//	else
		//	{
		//	console.log("\033[35;1m [ NotOk ] Username throw status not ok ");
	//	}

	
		
	})
}
//Make the uName function....
function checkUser(uName){
	// Define the social media urls...
	let facebook = `https://www.facebook.com/${uName}`
	let instagram = `https://instagram.com/${uName}`
	let twitter = `https://m.twitter.com/${uName}`
	//let youtube = `https://www.youtube.com/c/${uName}`
	let github = `https://www.github.com/${uName}`
	//let linkedin = `https://www.linkedin.com/in/${uName}`
	let pinterest = `https://www.pinterest.com/${uName}`
	//let medium = `https://medium.com/@${uName}`
	let reddit = `https://reddit.com/u/${uName}`
	let telegram = `https://t.me/${uName}`
	let vimeo = `https://vimeo.com/${uName}`
	//Make a array
	let social = [ facebook,instagram,twitter,github,pinterest,reddit,telegram,vimeo]
social.forEach((urls)=>{
	console.log("\n");
	isOk(urls);

});


}
//Halndle the User Argument...
if(process.argv.length < 3){
	help();
}
else if (process.argv[2] === "-h" || process.argv[2] === "--help"){
	help();

}
else
{
console.log("\033[32;1m [~] \033[36;1m Searching username wait...");
	const uName = process.argv[2]
	checkUser(uName);
}









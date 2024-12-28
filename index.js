function getNumber() {
	let number;
	while (true) {
		try {
			number = prompt("What is number? ");
		} catch {
			console.log("number is not an integer");
		}
		return number;
	}
}

const numb = getNumber();
console.log(`x is ${numb}`);

// let numb = prompt("What's number? ")
// console.log(numb);

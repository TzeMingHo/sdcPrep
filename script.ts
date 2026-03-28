import fs from 'node:fs/promises';

interface Player {
    name: string;
    score: number;
}

const data = await fs.readFile("./data.json", "utf-8")
const scores = JSON.parse(data) as Player[];

// What was the name of the first person to play the game?
console.log(scores[0]?.name)

// What was the name of the last person to play the game?
console.log(scores[scores.length - 1]?.name)

// Who had the highest score?
console.log([...scores].sort((a, b) => a.score - b.score)[scores.length - 1]?.name)

// The names of everyone who played the game directly after Daniel?
scores.forEach((player, index) => {
    if (player.name === "Daniel") {
        console.log(scores[index + 1]?.name)
    }
})


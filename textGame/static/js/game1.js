const textElement = document.getElementById('text');
const optionButtonsElement = document.getElementById('option-buttons');

let state = {};

function startGame() {
  state = { insects: false, amphibians: false, mammals: false, plants: false };
  showTextNode(1);
}

function showTextNode(textNodeIndex) {
  const textNode = textNodes.find(textNode => textNode.id === textNodeIndex);
  textElement.innerText = textNode.text;
  while (optionButtonsElement.firstChild) {
    optionButtonsElement.removeChild(optionButtonsElement.firstChild);
  }

  textNode.options.forEach(option => {
    const button = document.createElement('button');
    button.innerText = option.text;
    button.classList.add('btn');
    button.addEventListener('click', () => selectOption(option));
    optionButtonsElement.appendChild(button);
  });
}

function selectOption(option) {
  const nextTextNodeId = option.nextText;
  state = Object.assign(state, option.setState);

  if (nextTextNodeId === 5) { // Assuming the 5th node is for reflection/ending
    checkCompletion(); // Check if all types were selected before showing the ending
  } else {
    showTextNode(nextTextNodeId);
  }
}
function checkCompletion() {
  if (state.insects && state.amphibians && state.mammals && state.plants) {
    showTextNode(6); // Success node
    document.getElementById('score').style.display = 'block';
  } else {
    showTextNode(7); // Failure node, allowing for a retry
  }
}

function selectOption(option) {
  const nextTextNodeId = option.nextText;

  if (nextTextNodeId === null) {
    window.close();
    return;
  }

  state = Object.assign(state, option.setState);

  showTextNode(nextTextNodeId);
}

const textNodes = [
  {
    id: 1,
    text: 'If you were to establish a wildflower meadow here, as an ecologist, what would you introduce first?',
    options: [
      { text: 'Introduce Butterflies and bees', setState: { insects: true }, nextText: 2 },
      { text: 'Introduce Frogs and Toads', setState: { amphibians: true }, nextText: 2 },
      { text: 'Introduce Rabbits,Foxes and Voles', setState: { mammals: true }, nextText: 2 },
      { text: 'Introduce fritillaria and cornflower', setState: { plants: true }, nextText: 2 }
    ]
  },
  {
    id: 2,
    text: 'What would you like to introduce next?',
    options: [
      { text: 'Introduce Butterflies and bees', setState: { insects: true }, nextText: 3 },
      { text: 'Introduce Frogs and Toads', setState: { amphibians: true }, nextText: 3 },
      { text: 'Introduce Rabbits,Foxes and Voles', setState: { mammals: true }, nextText: 3 },
      { text: 'Introduce fritillaria and cornflower', setState: { plants: true }, nextText: 3 }
    ]
  },
  {
    id: 3,
    text: 'The meadow is taking shape. What’s next?',
    options: [
      { text: 'Introduce Ladybugs and dragonfiles', setState: { insects: true }, nextText: 4 },
      { text: 'Introduce Frogs and Toads', setState: { amphibians: true }, nextText: 4 },
      { text: 'Introduce Deer and Squirrels', setState: { mammals: true }, nextText: 4 },
      { text: 'Introduce poppy,nettle and orchid', setState: { plants: true }, nextText: 4 }
    ]
  },
  {
  id: 4,
  text: 'One last step. What will complete your ecosystem?',
  options: [
    { text: 'Introduce Ladybugs and dragonfiles', setState: { insects: true }, nextText: 5 },
    { text: 'Introduce Frogs and Toads', setState: { amphibians: true }, nextText: 5 },
    { text: 'Introduce Deer and Squirrels', setState: { mammals: true }, nextText: 5 },
    { text: 'Introduce poppy,nettle and orchid', setState: { plants: true }, nextText: 5 }
  ]
},

  {
    id: 5,
    text: 'Your grassland ecosystem is now complete. How do you feel about your choices?',
    options: [
      { text: 'Reflect on the ecosystem', setState: {}, nextText: 6 },
    ]
  },
  {
    id: 6,
    text: 'Congratulations! Your meadow is thriving with a diverse ecosystem.',
    options: [
    { text: 'Close Window', setState: {}, nextText: null }
  ]
  },
  {
    id: 7,
    text: 'Your meadow is missing some key biodiversity. Would you like to try again?',
    options: [
      { text: 'Restart', setState: { insects: false, amphibians: false, mammals: false, plants: false }, nextText: 1 }
    ]
  }
];


startGame();

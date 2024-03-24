const textElement = document.getElementById('text');
const optionButtonsElement = document.getElementById('option-buttons');

let state = {};

// Initializes the game state and starts the game by showing the first text node.
function startGame() {
  // Initializing state with false values for each category.
  state = { insects: false, amphibians: false, mammals: false, plants: false };
  // Display the first text node to the player.
  showTextNode(1);
}

// Displays the text node based on the given index.
function showTextNode(textNodeIndex) {
  // Finds the text node from the array of text nodes by matching the id.
  const textNode = textNodes.find(textNode => textNode.id === textNodeIndex);
  // Sets the main text element to display the found text node's text.
  textElement.innerText = textNode.text;
  // Removes all existing option buttons to prepare for new ones.
  while (optionButtonsElement.firstChild) {
    optionButtonsElement.removeChild(optionButtonsElement.firstChild);
  }

  // For each option in the current text node, create and display an option button.
  textNode.options.forEach(option => {
    const button = document.createElement('button'); // Creates a new button element.
    button.innerText = option.text; // Sets the button text to the option's text.
    button.classList.add('btn'); // Adds a class for styling the button.
    // Adds an event listener to the button that will call selectOption when clicked.
    button.addEventListener('click', () => selectOption(option));
    // Adds the newly created button to the page.
    optionButtonsElement.appendChild(button);
  });
}

function selectOption(option) {
  const nextTextNodeId = option.nextText;
  // Update the game state with the selected option's state changes
  state = Object.assign(state, option.setState);

  // If there is no next text node (nextTextNodeId is null), try to close the window
  if (nextTextNodeId === null) {
    window.close();
    return; // Stop the function execution here
  }

  // Special case: If the next node is node 5, check if the ecosystem is complete
  // before showing the ending
  if (nextTextNodeId === 5) {
    checkCompletion(); // Check if the ecosystem completion conditions are met
  } else {
    // For all other cases, proceed to show the next text node as per the player's choice
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
    { text: 'Back to adventure!', setState: {}, nextText: null }
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

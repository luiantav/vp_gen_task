var questions = {
  0: {
    prompt: '<h2>What is the colour of a ripe lemon?</h2>'+
    '<p>We are asking for the color of a ripe lemon, and not the colour of a lime.</p>'+
    '<p>We care about you reading the instructions carefully.</p>' +
    '<p>In order to demonstrate that, make sure to select green as your answer below.</p>',
    options: ["blue", "yellow", "green", "red"],
    correct_answer: 'green'},
  1: {
    prompt: '<h2>What does a mouse prefer to eat?</h2>'+
    '<p>According to popular belief, mice supposedly love cheese.</p>'+
    '<p>However, researchers found that mice do not like cheese at all. Instead they prefer sugary foods, such as fruit.</p>',
    options: ["cheese", "insects", "bacon", "fruit"],
    correct_answer: 'fruit'},
  2: {
    prompt: '<h2>Can cats see in complete darkness?</h2>'+
    '<p>Cats are able to see in very low light which makes them excellent night time hunters.</p>'+
    '<p> Even though it is often believed that cats can see in complete darkness, it is not correct.</p>'+
    '<p>They require at least some source of light to be able to see.</p>',
    options: ["yes", "no"],
    correct_answer: 'no'},
  3: {
    prompt: '<h2>Dogs can see colour?</h2>'+
    '<p>It is sometimes believed that dogs can only see black and white, but that is not true. </p>'+
    '<p> They are red-green colour blind though and they are unable to see fine details. </p>'+
    'Yet, that doesn\'t mean that dogs are poor at navigating around places. </p>'+
    'Instead of relying mainly on vision, dogs have a formidable sense of smell which allows them to make sense of their surroundings.</p>',
    options: ["yes", "no"],
    correct_answer: "yes"},
};

var attention_checks = [];

for (var x = 0; x < Object.keys(questions).length; x++) {
  attention_checks[x] = {
    type: jsPsychSurveyMultiChoice,
    questions: [{
      prompt: questions[x].prompt,
      name: x,
      options: questions[x].options,
      required: true }],
      data: {type: 'attention_check', correct_answer: questions[x].correct_answer, name: x},
      on_finish: function(data) {
        var correct_answer = data.correct_answer;
        if (data.response[data.name] == data.correct_answer) {
          data.correct = true;
          console.log(data.correct)
        } else {
          data.correct = false;
          console.log(data.correct)
        }
      }
    };
};

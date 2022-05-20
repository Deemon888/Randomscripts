const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

// lib ^^^

let x = context.params.event.data.options[0].value
let eq = context.params.event.data.options[1].value
let y = context.params.event.data.options[2].value

// options ^^^

let nx = parseInt(x)
let ny = parseInt(y)

let add = (nx + ny)
let sub = (nx - ny)
let mul = (nx * ny)
let div = (nx / ny)

// int vars ^^^

let chan = context.params.event.channel_id
let user = context.params.event.member.user.username
let user_id = context.params.event.member.user.id

// vars ^^^

if (`${eq}` === '+' || `${eq}` === 'add') {
  await lib.discord.channels['@0.1.1'].messages.create ({
    channel_id: chan,
    content: `<@${user_id}> \n\n` + nx + ' + ' + ny + ' = ' + add
  });
  // add ^^^
  console.log(`user : ${user}\n${nx} + ${ny}\nanswer : ${add}`);
} if (`${eq}` === '-' || `${eq}` === 'sub') {
  await lib.discord.channels['@0.1.1'].messages.create ({
    channel_id: chan,
    content: `<@${user_id}> \n\n` + nx + ' - ' + ny + ' = ' + sub
  });
  // sub ^^^
  console.log(`user : ${user}\n${nx} - ${ny}\nanswer : ${sub}`);
} if (`${eq}` === 'x' || `${eq}` === '*' || `${eq}` === 'mul') {
  await lib.discord.channels['@0.1.1'].messages.create ({
    channel_id: chan,
    content: `<@${user_id}> \n\n` + nx + ' x ' + ny + ' = ' + mul
  });
  // mul ^^^
  console.log(`user : ${user}\n${nx} x ${ny}\nanswer : ${mul}`);
} if (`${eq}` === '/' || `${eq}` === 'div') {
  await lib.discord.channels['@0.1.1'].messages.create ({
    channel_id: chan,
    content: `<@${user_id}> \n\n` + nx + ' / ' + ny + ' = ' + div
  });
  // div ^^^ ( not the tag :) )
  console.log(`user : ${user}\n${nx} / ${ny}\nanswer : ${div}`);
}

// script/command ^^^ 

// this is not that much but ^^^ it works 

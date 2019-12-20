  var csrftoken = Cookies.get('csrftoken');
    console.log(csrftoken)
      function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
      }
      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        }
      });


    //initializing some variables
    var botui;
        var init=0;
    var s,res,inputdata;
    chatbot=document.getElementById('chatbot')


    //clicking chating img
    document.getElementById('chat_img').onclick = function(){
        if(window.getComputedStyle(chatbot).display == 'none'){
        chatbot.style.display='block';
        document.getElementById('arrow_id').style.display='none';
        if(init==0){
            initialize()
        }
    }
     else{
        chatbot.style.display='none';
        document.getElementById('arrow_id').style.display='block';
    }
}


//onclick of enter or send button
function ex_func(e){
    s=document.getElementById('textbox').value
    inputdata={
    'text':s
    }
    console.log(inputdata)
    botui.message.human({
        photo:'static/images/fred.png',
        content:''+s,
    })
   document.getElementById('textbox').value=''
}
//on pressing enter key
document.addEventListener('keypress',function(e){
    if(e.keyCode==13){
        ex_func(document.getElementById('textbox').value)
    }
})
//initial message function
function initialize(){
   botui = new BotUI('my-botui-app')
   console.log(botui)
   init=1
}
//response to the user input
$('#form').submit(send_data)
$('#send_btn').click(send_data)
//ajax call to django server on enter or button click
function send_data(event){
event.preventDefault()
  $.ajax({
      type: 'POST',
      url: 'api/chatterbot/',
      data: JSON.stringify(inputdata),
      contentType: 'application/json',
      success:output
})
}
//ajax call on button click given by the bot
function button_click(res){
 $.ajax({
     type: 'POST',
     url: 'api/chatterbot/',
     data: JSON.stringify(inputdata),
     contentType: 'application/json',
     success:output
  })
}
//onclicking refresh button
$('.refresh').click(function(){
    while(document.getElementById('chat').firstChild){
    document.getElementById('chat').removeChild(document.getElementById('chat').firstChild)
    }
    document.getElementById('chat').insertAdjacentHTML('afterbegin','<div id="my-botui-app"></div>')
    document.getElementById('my-botui-app').insertAdjacentHTML('afterbegin','<bot-ui id="bot"></bot-ui>')
    initialize()
})


//function that is executed on success of the ajax request
function output(resp)
{
if('url' in resp){
botui.message.bot({
    loading:true,
    delay:1000,
    photo:'static/images/Capture.png',
    content:resp.text
}).then(function(){
botui.message.bot({
    photo:'static/images/Capture.png',
    content:`[click here](${resp.url})`
})
})
}
else{
botui.message.bot({
    loading:true,
    delay:1000,
    photo:'static/images/Capture.png',
    content:resp.text
})
}
}
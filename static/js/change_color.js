function getColorToChange() {
  var textInput = document.getElementById('text_input').value
  var lightList = document.getElementById('list_of_lights').value

  $.ajax({
    type: 'POST',
    contentType: "application/json; charset=utf-8",
    url: '/change_color',
    async: true,
    data: JSON.stringify({
      text_input: textInput,
      lights: lightList
    }),
    success: (response) => {
      color = response.rgb;
    },
    error: (response) => {
      alert('That did not work. Enter text where it says text. Seperate lights by commas.')
    }
  })
}

function connectBridge() {
  console.log("connect to bridge")
  $.ajax({
    type: 'POST',
    contentType: "application/json; charset=utf-8",
    url: '/connect_bridge',
    success: (response) => {
      console.log('Bridge connected.')
    },
    error: (response) => {
      alert('Bridge failed to connect!')
    }
  })
}
const socket = io('http://localhost:3000')
const messageContainer = document.getElementById('message-container')
const messageForm = document.getElementById('send-container')
const messageInput = document.getElementById('message-input')
const roomContainer = document.getElementById('room-container')

if (messageForm != null) {
  const name = prompt('You are entering a public room. Enter the name you want to be identified by.',"Anonymous")
  appendMessage('<center><by>You</by> joined</center>')
  socket.emit('new-user', roomName, name)

  messageForm.addEventListener('submit', e => {
    e.preventDefault()
    const message = messageInput.value
    appendMessage(`<by>You</by><br>${message}`)
    socket.emit('send-chat-message', roomName, message)
    messageInput.value = ''
  })
}

socket.on('room-created', room => {
  const roomElement = document.createElement('div')
  roomElement.innerText = room
  const roomLink = document.createElement('a')
  roomLink.href = `/${room}`
  roomLink.innerText = 'join'
  roomContainer.append(roomElement)
  roomContainer.append(roomLink)
})

socket.on('chat-message', data => {
  appendMessage(`<by>${data.name}</by><br>${data.message}`)
})

socket.on('user-connected', name => {
  appendMessage(`<center><by>${name}</by> connected</center>`)
})

socket.on('user-disconnected', name => {
  appendMessage(`<center><by>${name}</by> disconnected</center>`)
})

function appendMessage(message) {
  const messageElement = document.createElement('div')
  messageElement.innerHTML = message
  messageContainer.append(messageElement)
}
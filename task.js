fetch('http://127.0.0.1:5000/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    cities: ['Chandigarh', 'Delhi']
  })
})
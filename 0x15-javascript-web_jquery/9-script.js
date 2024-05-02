$.ajax({
  type: 'GET',
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: function (response) {
    $('DEV#hello').append(response.hello);
  }
});

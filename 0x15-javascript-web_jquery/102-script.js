addEventListener("load", () => {
  $('INPUT#btn_translate').click(() => {
    const languageCode = $('INPUT#language_code').text();
    console.log(languageCode);
    const reqUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;
    $.get(reqUrl,
      function (data, textStatus) {
        $('DIV#hello').text(data.hello);
      });
  });
});

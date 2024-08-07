$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data, textStatus) {
    for (const potato of data.results) {
      const movieTitleListing = '<li>' + potato.title + '</li>';
      $('UL#list_movies').append(movieTitleListing);
    }
  });

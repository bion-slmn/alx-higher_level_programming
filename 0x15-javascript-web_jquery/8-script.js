const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  const movies = data.results;
  for (const index in movies) {
    $('ul#list_movies').append('<li>' + movies[index].title + '</li>');
  }
});

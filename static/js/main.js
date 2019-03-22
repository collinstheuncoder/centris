$(() => {
	// Dropdown on hover
	$('.dropdown-trigger').dropdown({
    hover: true,
    inDuration: 300,
    outDuration: 225,
    constrainWidth: false,
  });

  // Price range slider
  // const slider = document.getElementById('price-slider');

  // noUiSlider.create(slider, {
  //   start: [0, 100000],
  //   connect: true,
  //   step: 1000,
  //   range: {
  //     'min': 0,
  //     'max': 20000000
  //   },
  //   format: wNumb({
  //     decimals: 0
  //   })
  // });

  // Toggle search options
  // 1. By Property Type
  $('.options--type > .option-btn').on('click', () => {
    $('.options--type > .option-btn').toggleClass('option-btn--selected');
  });

  // 2. By Sale or Rent
  $('.options--price > .option-btn').on('click', () => {
    $('.options--price > .option-btn').toggleClass('option-btn--selected');
  });

  // Toggle advanced settings
  $('#toggle-advanced').on('click', () => {
    $('.advanced-settings').toggle();
    $('#toggle-advanced > .fas').toggleClass('fa-chevron-down');
    $('#toggle-advanced > .fas').toggleClass('fa-chevron-up');
  });

  // Select menu
  $('select').formSelect();

  // Tabs
  $('.tabs').tabs();

  // Footer year
	const year = new Date().getUTCFullYear();

	$('#footer-year').text(year);
});

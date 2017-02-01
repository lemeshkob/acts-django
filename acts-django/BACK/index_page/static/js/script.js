const SLIDER_CHANGE_INTERVAL = 7000; // imprtant, SLIDER_CHANGE_INTERVAL > 1200

document.addEventListener('DOMContentLoaded', function() {
	
	var pedInfoMore = Array.from(document.querySelectorAll('.ped__info__more'));
	if (pedInfoMore.length > 0) {
		pedInfoMore.map(function(el) {
			el.querySelector('.ped__info__more__open').addEventListener('click', function() {
				var flag = false;
				if (el.classList.contains('ped__info__more_active')) {
					flag = true;
				}

				Array.from(document.querySelectorAll('.ped__info__more_active')).map(function(el) {
					el.classList.remove('ped__info__more_active');
				})

				if (flag !== true) {
					el.classList.add('ped__info__more_active');
				}
			})
		})
	}

	var slides = Array.from(document.querySelectorAll('.slider__slider>ul'));
	var cliderCircles = [];
	if (slides.length > 1) {
		var prevSlide = 0,
			activeSlide = 0;

		slides.map((el, index) => {
			var circle = document.createElement('ul');
			circle.classList.add('slider__circle');

			if (index === 0) {
				el.classList.add('slider__slide_active');
				circle.classList.add('slider__circle_active');
			} else {
				el.classList.add('slider__slide_disabled');
			}

			document.querySelector('.slider__circles').appendChild(circle);
			cliderCircles.push(circle);
		});

		setInterval(() => {
			prevSlide = activeSlide;
			activeSlide++;

			if (activeSlide === slides.length) {activeSlide = 0;};
			slides[activeSlide].classList.add('slider__slide_animation');

			cliderCircles[prevSlide].classList.remove('slider__circle_active');
			cliderCircles[activeSlide].classList.add('slider__circle_active');

			setTimeout(() => {
				slides[activeSlide].classList.remove('slider__slide_animation');
				slides[prevSlide].classList.remove('slider__slide_active');
				slides[activeSlide].classList.add('slider__slide_active');
			}, 1200);
		}, SLIDER_CHANGE_INTERVAL);
	}
})
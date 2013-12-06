function GetWeatherForLocation(lat, lon, divName)
	{
	   /*uses ajax function and the wunderground weather.com API to retrieve information */
	   console.log("entered weather");
		var results;
		northgateLat = 30.616703;
		northgateLng = -96.333544;
		results = $.ajax({
		   url:
		   "http://api.wunderground.com/api/44436df8c5396f7d/geolookup/conditions/q/"+lat+","+lon+".json",
		  dataType: "jsonp",
		  async: false,
				   success : function(parsed_json) {
				   /*wunderground API returns inforomation in json format, 
					take information from json and store it into variables for use*/
						var location = parsed_json['location']['city'];
						var zip = parsed_json['location']['zip'];
						var realTemp_f = parsed_json['current_observation']['temp_f'];
						var realTemp_c = parsed_json['current_observation']['temp_c'];
						var feelsLike_f = parsed_json['current_observation']['feelslike_f'];
						var feelsLike_c = parsed_json['current_observation']['feelslike_c'];
						var wind = parsed_json['current_observation']['wind_mph'];
						var humidity = parsed_json['current_observation']['relative_humidity'];
						var precip = parsed_json['current_observation']['precip_today_string'];
						var weather = parsed_json['current_observation']['weather'];
						var weatherpic = parsed_json['current_observation']['icon_url'];
						/*put the weather information into an array that can be used to make a marker*/
						/*
						var things = new Array();
						things.push(location);
						things.push(zip);
						things.push(realTemp_f);
						things.push(realTemp_c);
						things.push(feelsLike_f);
						things.push(feelsLike_c);
						things.push(wind);
						things.push(humidity);
						things.push(precip);
						things.push(weather);
						things.push(weatherpic);
						*/
						//change the text of weatherDiv
						var div = document.getElementById(divName);
						console.log(weather);
						div.textContent = realTemp_f + "f - " + weather;
						if(divName == "geoDiv")
						{
							var div2 = document.getElementById("curLoc");
							div2.textContent = location + " ";
						}
				   }
			   });

			return results;
	}

	function showPosition(position)
	{
		var latitude = position.coords.latitude;
		var longitude = position.coords.longitude;
		GetWeatherForLocation(latitude,longitude,"geoDiv");
	}
	function getLocation()
	{
		if(navigator.geolocation)
		{
			navigator.geolocation.getCurrentPosition(showPosition);
		}
		else
		{
			//nothing
		}
	}
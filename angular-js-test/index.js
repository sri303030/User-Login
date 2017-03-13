'use strict';

angular.module('myLogin', [])
	.controller('LoginController', ['$scope', '$http', '$q',
		function($scope, $http, $q){
		$scope.login = function(){
			log($scope.userName, $scope.password).then(function(ack) {
				if(ack === 'Success') {
					alert('Login Success!');
				} else {
					alert('Login fail: ' + ack);
				}
			}, function(err) {
				alert(err);
			});
		};

		var log = function(userName, password) {
			var data = {
				'userName': userName,
				'password': password
			};
			var url = "/api/v1/login";
			var http = $http['post'](url, data);
			var deferred = $q.defer();
			http.success(function(ack){
				deferred.resolve(ack);
			});
			return deferred.promise;
		};

	}])
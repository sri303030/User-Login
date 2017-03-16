'use strict';

angular.module('myLogin', [])
	.controller('LoginController', ['$scope', 'LoginService',
		function($scope, LoginService) {

		$scope.login = function() {
			LoginService.log($scope.userName, $scope.password).then(function(ack) {
				if(ack === 'Success') {
					alert('Login Success!');
				} else {
					alert('Login fail: ' + ack);
				}
			}, function(err) {
				alert(err);
			});
		};

	}]);
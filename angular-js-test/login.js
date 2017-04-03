'use strict';

angular.module('myApp',['ui.router'])
	.controller('LoginController', ['$scope', '$state', 'LoginService',
		function($scope, $state, LoginService) {

			$scope.login = function() {
				LoginService.log($scope.userName, $scope.password).then(function(ack) {
					if(ack.result === 'Success') {
						alert('Login Success!');
					} else {
						alert('Login fail: ' + ack);
					}
				}, function(err) {
					alert(err);
				});
			};

			$scope.goHistory = function() {
				$state.go('history');
			};

		}
	])
	.controller('HistoryController', ['$scope', '$state', 'LoginService',
		function ($scope, $state, LoginService) {
			$scope.goHome = function() {
				$state.go('login');
			};

			$scope.historyUsers = [];

			getUsers();

			function getUsers() {
				LoginService.history().then(function(ack) {
					$scope.historyUsers = angular.copy(ack.users);
				}, function(err){
					alert(err);
				});
			}
		}
	])
	.config(['$stateProvider', '$urlRouterProvider',
		function($stateProvider, $urlRouterProvider) {
			$urlRouterProvider.otherwise('/');
			$stateProvider
				.state('login',{
					url: '/',
					templateUrl: 'login.html',
					controller: 'LoginController'
				})
				.state('history', {
					url: '/history',
					templateUrl: 'login-history.html',
					controller: 'HistoryController'
				});
		}
	]);
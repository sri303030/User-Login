'user strict';

angular.module('myApp')
    .service('LoginService', ['$http', '$q',
    function($http, $q) {

    this.log = function(userName, password) {
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

    this.history = function () {
        var url = '/api/v1/users';
        var http = $http['get'](url);
        var deferred = $q.defer();
        http.success(function (ack) {
            deferred.resolve(ack);
        });
        return deferred.promise;
    };

}]);
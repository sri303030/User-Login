'user strict';

angular.module('myLogin')
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

}]);
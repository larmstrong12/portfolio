'use strict';

angular.module('myApp.contact', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/contact', {
            templateUrl: 'contact/contact.html',
            controller: 'ContactCtrl'
        });
    }])

    .controller('ContactCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {

        $scope.contact = function () {
            Restangular.all('contact').customPOST($scope.contact).then(function () {
                toastr.success("You successfully sent the message!");
                $scope.$apply();
                $scope.contact.photo = null;
            }, function () {
                toastr.error("There was a problem sending your message");
            });
        };
    }]);

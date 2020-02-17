const {Constants}  =  require('eae-utils');

module.exports = {
    mongoURL: 'mongodb://mongodb/opal',
    port: 80,
    enableCors: true,
    swiftURL: 'http://swift:8080',
    swiftUsername: 'test:tester',
    swiftPassword: 'testing',
    computeType: [Constants.EAE_COMPUTE_TYPE_PYTHON2],
    clusters:{}
};

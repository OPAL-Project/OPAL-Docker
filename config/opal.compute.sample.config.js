const {Constants}  =  require('eae-utils');

module.exports = {
    mongoURL: 'mongodb://mongodb/opal',
    timescaleURL: 'postgres://postgres@timescaledb/opal',
    port: 80,
    enableCors: true,
    computeType: [Constants.EAE_COMPUTE_TYPE_PYTHON2],
    opalAlgoServiceURL: 'http://algoservice:80',
    opalAggPrivServiceURL: 'http://aggandprivacy:80',
    opalalgoSandboxVenv: '/usr/venv/sandbox',
    opalalgoSandboxUser: 'sandbox',
    maxUsersPerFetch: 5000,
    maxCores: 7,
    randomSeed: 0.42 // should be between -1 and 1
};

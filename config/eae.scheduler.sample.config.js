
module.exports = {
    mongoURL: 'mongodb://mongodb/opal',
    port: 80,
    enableCors: true,
    archivingEnabled: false,
    jobsExpiredStatusTime: 720 , // Time in hours: 24h * 30d. Jobs to be archived
    jobsTimingoutTime: 24 , // Time in hours: 24h. Jobs to be cancelled for exceeding computing time policy.
    nodesExpiredStatusTime: 1, // Time in hours. Tolerance for the refresh of the nodes' status
    swiftURL: 'http://swift:8080',
    swiftUsername: 'test:tester',
    swiftPassword: 'testing'
};

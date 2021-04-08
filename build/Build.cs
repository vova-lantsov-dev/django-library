using Nuke.Common;
using Nuke.Common.CI.TeamCity;
using Nuke.Common.IO;
using Nuke.Common.Tooling;

[TeamCity(TeamCityAgentPlatform.Unix, ManuallyTriggeredTargets = new[] {nameof(Down)}, VcsTriggeredTargets = new[] {nameof(Up)}, Version = "2020.2")]
class Build : NukeBuild
{
    /// Support plugins are available for:
    ///   - JetBrains ReSharper        https://nuke.build/resharper
    ///   - JetBrains Rider            https://nuke.build/rider
    ///   - Microsoft VisualStudio     https://nuke.build/visualstudio
    ///   - Microsoft VSCode           https://nuke.build/vscode

    public static int Main () => Execute<Build>(x => x.Up);

    [Parameter("Configuration to build - Default is 'Debug' (local) or 'Release' (server)")]
    readonly Configuration Configuration = IsLocalBuild ? Configuration.Debug : Configuration.Release;

    [Parameter("The name of docker-compose project")]
    readonly string ProjectName = "django-library";
    
    [PathExecutable("docker-compose")]
    readonly Tool DockerCompose;
    
    AbsolutePath SourceDirectory => RootDirectory / "src";

    Target Down => _ => _
        .Executes(() =>
        {
            DockerCompose($"-p {ProjectName} down", SourceDirectory);
        });
    
    Target Up => _ => _
        .DependsOn(Down)
        .Executes(() =>
        {
            DockerCompose($"-p {ProjectName} up --build -d", SourceDirectory);
        });

}

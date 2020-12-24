%this is the image of all 1000 trials
load ("Ch2-EEG-1.mat")
ntrials = size(EEGa,1)
imagesc(t,[1:ntrials],EEGa);
xlabel("Time [s]")
ylabel("Trial #")
hold on
plot([0.25 0.25],[0 1000],'k','LineWidth',2)
hold off
--------------------------------------------------------------------------------
%计算所有trial的平均
load ("Ch2-EEG-1.mat")
plot(t, mean(EEGa,1));
xlabel("Time [s]")
ylabel("Votage [\mu V]")
title("ERP of condition A")
hold on
plot([0.25 0.25],[-0.5 0.5],'k','LineWidth',2)
hold off
load ("Ch2-EEG-1.mat")
hold on
plot(t, mean(EEGb,1));
hold off
---------------------------------------------------------------------------------
%比较两种条件下的相交
load ("Ch2-EEG-1.mat")
ntrials = size(EEGa,1)
mnA = mean(EEGa,1)
sdmnA = std(EEGa,1)/sqrt(ntrials)
mnB = mean(EEGb,1)
sdmnB = std(EEGb,1)/sqrt(ntrials)
sdmnD = sqrt(sdmnA .^2 + sdmnB .^2)
plot(t,mnA,'LineWidth',3)
hold on
plot(t,mnA+2*sdmnD)
plot(t,mnA-2*sdmnD)
plot(t,zero(size(mnA)),'k')
hold off
----------------------------------------------------------------------------------
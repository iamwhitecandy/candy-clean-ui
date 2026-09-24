package com.servercandy.cleanui;

import net.fabricmc.api.ClientModInitializer;

public class CandyCleanUiClient implements ClientModInitializer {
    @Override
    public void onInitializeClient() {
        System.out.println("[CandyCleanUI] Initialized: Toast suppressor active (advancements, recipes, unsecure server warning disabled).");
    }
}

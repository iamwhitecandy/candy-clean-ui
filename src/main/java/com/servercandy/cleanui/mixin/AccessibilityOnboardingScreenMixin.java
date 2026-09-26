package com.servercandy.cleanui.mixin;

import net.minecraft.class_8032;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

@Mixin(class_8032.class)
public class AccessibilityOnboardingScreenMixin {
    @Inject(method = "method_25426", at = @At("HEAD"), cancellable = true)
    private void candySkipAccessibilityOnboarding(CallbackInfo ci) {
        ((class_8032) (Object) this).method_25419();
        ci.cancel();
    }
}

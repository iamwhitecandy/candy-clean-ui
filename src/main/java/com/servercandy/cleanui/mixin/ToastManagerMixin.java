package com.servercandy.cleanui.mixin;

import net.minecraft.class_366;
import net.minecraft.class_367;
import net.minecraft.class_368;
import net.minecraft.class_370;
import net.minecraft.class_372;
import net.minecraft.class_374;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

@Mixin(class_374.class)
public class ToastManagerMixin {
    @Inject(method = "method_1999", at = @At("HEAD"), cancellable = true)
    private void suppressIntrusiveToasts(class_368 toast, CallbackInfo ci) {
        // Suppress recipe unlocks, advancements, and tutorial popups
        if (toast instanceof class_367 || toast instanceof class_366 || toast instanceof class_372) {
            ci.cancel();
            return;
        }

        // Suppress unsecure server warning system toast ("Невозможно проверить сообщения чата...")
        if (toast instanceof class_370 systemToast) {
            if (systemToast.method_1989() == class_370.class_9037.field_47589) {
                ci.cancel();
            }
        }
    }
}

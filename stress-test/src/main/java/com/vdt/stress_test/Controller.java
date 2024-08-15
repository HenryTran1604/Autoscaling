package com.vdt.stress_test;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class Controller {
    @GetMapping("/stress")
    public int stress() {
        int count = 0;
        for(int i = 0; i < 5000000; i++) {
            count += 1;
        }
        return count;
    }
}
